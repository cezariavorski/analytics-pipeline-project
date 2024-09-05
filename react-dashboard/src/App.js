import React, { useState, useEffect } from 'react';

function Dashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/data')
      .then(response => response.json())
      .then(data => setData(data.users));
  }, []);

  return (
    <div>
      <h1>User Data</h1>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Age (Months)</th>
            <th>City</th>
          </tr>
        </thead>
        <tbody>
          {data.map((user, index) => (
            <tr key={index}>
              <td>{user.name}</td>
              <td>{user.age_in_months}</td>
              <td>{user.city}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Dashboard;
