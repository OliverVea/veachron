import React, {useEffect, useState} from 'react';

function App() {
  const url = 'http://localhost/api/Timings/list_timings'
  const [timings, setTimings] = useState([{}])

  useEffect(() => {
    fetch(`${url}`).then(
      res => res.json()
    ).then(
      data => {
        setTimings(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <div>
      
    </div>
  );
}

export default App;
