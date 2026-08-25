import { useState, useEffect } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      //setCount((prevCount) => prevCount + 1); // Using a callback function
    }, 1000);
    return () => clearInterval(interval);
  }, []); // Runs only on mount

  return <h1>Count: {count}</h1>;
}
