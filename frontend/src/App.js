import React, { useEffect, useState } from 'react';

import TimerListElement from './components/TimerListElement';

function App() {
  const hostname = 'http://api.localhost'
  const url = hostname + '/api/timers/list-timings'
  const [timings, setTimings] = useState([{}])

  useEffect(() => {
    fetch(`${url}`).then(
      res => res.json()
    ).then(
      data => {
        setTimings(data)
      }
    )
  }, []);

  return (
    <div style={{
      width: 'fit-content',
      maxWidth: '90%',
      margin: 'auto',
      display: 'flex',
      flexDirection: 'column',
      'justifyContent': 'center',
      height: '100%'
    }}>
      {(typeof (timings) === 'undefined') ? (
        <p>Loading...</p>
      ) : (
        <TimerListElement tree={[timings]} />
      )}
    </div>
  );
}

export default App;
