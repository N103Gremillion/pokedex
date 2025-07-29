export const HomeButton = () => {

  const handleClick = () => {
    console.log("Opening Home Page.")
  }

  return (
    <button 
      className="navbar-component"
      onClick={handleClick}
    >Home</button>
  );
}