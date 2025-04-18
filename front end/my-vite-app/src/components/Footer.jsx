const Footer = () => {
    return (
      <footer
        style={{
          marginTop: '4rem',
          padding: '1rem',
          backgroundColor: '#1a1a1a',
          color: '#ccc',
          textAlign: 'center',
          fontSize: '0.9rem',
        }}
      >
        
        <div style={{ marginBottom: '0.5rem' }}>
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
        <div style={{ fontSize: '0.8rem', color: '#888' }}>
          © {new Date().getFullYear()} Nicxx. All rights reserved.
        </div>
      </footer>
    );
  };
  
  export default Footer;
  