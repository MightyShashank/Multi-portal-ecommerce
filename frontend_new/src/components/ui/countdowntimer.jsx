import React, { useState, useEffect } from "react";

const CountdownTimer = ({ targetDate }) => {
  const [timeLeft, setTimeLeft] = useState({});

  // Function to calculate time difference
  const calculateTimeLeft = () => {
    const now = new Date();
    const difference = targetDate - now;

    if (difference <= 0) {
      return {
        days: 0,
        hours: 0,
        minutes: 0,
        seconds: 0,
      };
    }

    const days = Math.floor(difference / (1000 * 60 * 60 * 24));
    const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((difference % (1000 * 60)) / 1000);

    return { days, hours, minutes, seconds };
  };

  // Update the timer every second
  useEffect(() => {
    const interval = setInterval(() => {
      setTimeLeft(calculateTimeLeft());
    }, 1000);

    return () => clearInterval(interval); // Clean up the interval on unmount
  }, [targetDate]);

  return (
    <div className="flex items-center pt-0.5 space-x-2">
      <div className="text-sm text-gray-800 text-medium">Deals ends in</div>
      <div className="flex space-x-2 bg-yellow-400 py-1 px-4 rounded-md text-gray-800 font-medium text-sm">
        <span>{timeLeft.days}d</span>
        <span>{timeLeft.hours}h</span>
        <span>{timeLeft.minutes}m</span>
        <span>{timeLeft.seconds}s</span>
      </div>
    </div>
  );
};

// Usage of the Countdown Timer with a target date
const App = () => {
  const targetDate = new Date("2025-05-10T00:00:00").getTime(); // Set your target date here

  return (
    <div className="flex justify-center items-center">
      <CountdownTimer targetDate={targetDate} />
    </div>
  );
};

export default App;