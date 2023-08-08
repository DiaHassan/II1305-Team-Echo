import React, { useEffect } from 'react';
import axios from 'axios';

function Schedual() {
  const runFunction = () => {
    axios.post('https://rusty-quince-umuv-main-csa3pvckba-lz.a.run.app/test', {test: 30})
    .catch(error => console.log(error));
  };

  useEffect(() => {
    const now = new Date();
    const currentYear = now.getFullYear();
    const currentMonth = now.getMonth();

    // Calculate the last day of the current month
    const lastDayOfMonth = new Date(currentYear, currentMonth + 1, 0);

    // Calculate the execution date (3 days before the last day)
    const executionDate = new Date(lastDayOfMonth);
    executionDate.setDate(lastDayOfMonth.getDate() - 3);

    const timeUntilExecution = executionDate - now;

    if (timeUntilExecution > 0) {
      const timer = setTimeout(() => {
        runFunction();
      }, timeUntilExecution);

      // Clean up the timer when the component unmounts
      return () => {
        clearTimeout(timer);
      };
    }
  }, []);

  return (
    <div className="App">
      {/* Your JSX content */}
    </div>
  );
}

export default Schedual;
