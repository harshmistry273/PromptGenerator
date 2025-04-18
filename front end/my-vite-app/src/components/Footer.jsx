  const Footer = () => {
    return (
      <footer
        style={{
          marginTop: '4rem',
          padding: '1rem',
          backgroundColor: 'rgba(114, 114, 114, 0.24)',
          borderRadius:'10px',
          color: '#ccc',
          textAlign: 'center',
          fontSize: '0.9rem',
        }}
      >
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between', // Ensures space between text and image
            alignItems: 'center', // Aligns text and image vertically centered
            marginBottom: '0.5rem',
          }}
        >
          <div>
            <strong>Deployed by:</strong> Nicxx |{' '}
            <a
              href="https://github.com/Paradva-Niraj"
              target="_blank"
              rel="noopener noreferrer"
              style={{ color: '#666eff', textDecoration: 'none' }}
            >
              Contact
            </a>
          </div>
          <img
            src="/logo.png"
            alt="Logo"
            style={{ width: '50px', height: 'auto' }} // Adjusted size of the logo
          />
        </div>
        <div style={{ fontSize: '0.8rem', color: '#888' }}>
          © {new Date().getFullYear()} Nicxx. All rights reserved.
        </div>
      </footer>
    );
  };

  export default Footer;
