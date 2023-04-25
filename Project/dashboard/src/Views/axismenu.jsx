import React from 'react';
import './axismenu.css';

const ButtonList = ({ buttons }) => {
  return (
    <div className="button-list">
      {buttons.map(({ label, onClick }, index) => (
        <button key={index} onClick={onClick}>
          {label}
        </button>
      ))}
    </div>
  );
};

export default ButtonList;