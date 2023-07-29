import React, { useState } from 'react';

const WarningMessage = () => {
  const [showMessage, setShowMessage] = useState(true);

  const closeMessage = () => {
    setShowMessage(false);
  };

  if (!showMessage) {
    return null;
  }

  return (
    <div style={styles.warningMessage}>
      <p style={styles.messageText}>
        Statistikverktygen är fortfarande under utveckling, vilket kan leda till bugs. Var snäll och rapportera om det hittas.
      </p>
      <span style={styles.close} onClick={closeMessage}>
        &times;
      </span>
    </div>
  );
};

const styles = {
  warningMessage: {
    position: 'fixed',
    top: 0,
    right: 0,
    left: 0,
    width: '100%',
    height: '40px',
    backgroundColor: 'rgba(247, 63, 49, 0.8)',
    color: '#fff',
    padding: '10px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    zIndex: 9999, // Ensures the message stays on top of other elements
  },
  close: {
    cursor: 'pointer',
    fontSize: '30px',
    paddingRight: '10px'
  },
  messageText: {
    margin: 0,
    textAlign: 'center',
    flex: 1,
  },
};

export default WarningMessage;