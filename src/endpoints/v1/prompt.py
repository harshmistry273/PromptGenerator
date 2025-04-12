from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from src.utils.connection_manager import ConnectionManager
from src.utils.generate_prompt_from_data import GeneratePromptBot
from src.utils.logger import logger
from src.utils.check_prompt import check_prompt

router = APIRouter()
manager = ConnectionManager()
bot = GeneratePromptBot()

@router.websocket('/generate-prompt')
async def chat_for_prompt(websocket: WebSocket):
    try:
        logger.info("Initialized Prompt class")
        prompt_bot = GeneratePromptBot()

        logger.info("Establishing connection for client")
        await manager.connect(websocket)

        logger.info("Connection established")
        logger.info("Sending welcome message")
        await websocket.send_json(
            {
                "message": "Welcome to PromptAI",
                "data": [],
                "status": True,
                "error": ""
            }
        )

        while True:
            logger.info("Awaiting for data from client")
            data = await websocket.receive_json()

            logger.info(f"Processing message: {data["message"]}")
            user_message = data["message"]

            logger.info("Generating bot response for query")
            bot_response = prompt_bot.generate_prompt(query=user_message)

            if not bot_response:
                logger.info("Invalid bot response")
                await websocket.send_json(
                    {
                        "message": "An error occured, Please try again.",
                        "data": [],
                        "error": "",
                        "status": False
                    }
                )
                continue

            is_prompt_generated, prompt = check_prompt(bot_response)
            logger.info(f"Is prompt generated: {is_prompt_generated}")

            if is_prompt_generated:
                await websocket.send_json({
                "message": "Your prompt has been generated!",
                "data": prompt,
                "status": True,
                "error": ""
            })
                continue
            
            await websocket.send_json({
                "message": bot_response,
                "data": prompt,
                "status": True,
                "error": ""
            })

    except WebSocketDisconnect as e:
        logger.info("Connection closed for client")

    except Exception as e:
        logger.info(f"An exception occured: {str(e)}")
    
    finally:
        prompt_bot.clear_memory()
        logger.info("Memory cleared")

