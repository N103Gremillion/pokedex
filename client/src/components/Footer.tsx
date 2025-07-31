import React from 'react';

export const Footer = () => {
  return (
    <footer
      style={{
        textAlign: 'center',
      }}
    >
      © {new Date().getFullYear()} Your Site Name. All rights reserved.
    </footer>
  );
};
