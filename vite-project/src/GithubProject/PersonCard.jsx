import { useState, useEffect } from "react";
import axios from "axios";

function PersonCard({ person }) {
  const [followers, setFollowers] = useState([]);

  const { login, avatar_url, html_url, repos_url, followers_url } = person;

  const getFollowers = async () => {
    try {
      const response = await axios({
        method: "GET",
        url: followers_url,
        headers: {
          Authorization: `Bearer ${import.meta.env.VITE_GITHUB_TOKEN}`,
          Accept: "application/vnd.github+json",
        },
      });

      // Store the array of followers
      setFollowers(response.data);
    } catch (error) {
      console.error("Error fetching followers:", error);
    }
  };

  useEffect(() => {
    getFollowers();
  }, []);

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        marginTop: "20px",
        marginBottom: "20px",
        border: "2px solid rgba(0,0,0,0.1)",
        padding: "15px",
        borderRadius: "10px",
        boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
      }}
    >
      <img
        src={avatar_url}
        alt={login}
        style={{
          width: "100px",
          height: "100px",
          borderRadius: "50%",
        }}
      />

      <div
        style={{
          flex: 1,
          marginLeft: "20px",
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-evenly",
        }}
      >
        <div>
          <b style={{ fontSize: "20px" }}>{login}</b>
        </div>

        <div>Followers: {followers.length}</div>

        <div>
          <a href={html_url} target="_blank" rel="noreferrer">
            <button style={{ marginRight: "10px" }}>GitHub Profile</button>
          </a>

          <a href={repos_url} target="_blank" rel="noreferrer">
            <button>View Repositories</button>
          </a>
        </div>
      </div>
    </div>
  );
}

export default PersonCard;
