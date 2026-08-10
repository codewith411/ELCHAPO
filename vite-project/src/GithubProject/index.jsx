import { useState, useEffect } from "react";
import axios from "axios";

import TopNav from "./TopNav";
import InfoSection from "./InfoSection";
import PersonCard from "./PersonCard";

function GithubProject() {
  // State to store GitHub users
  const [people, setPeople] = useState([]);

  // Fetch GitHub users
  const getUserData = async () => {
    try {
      const response = await axios.get("https://api.github.com/users", {
        headers: {
          Authorization: `Bearer ${import.meta.env.VITE_GITHUB_TOKEN}`,
        },
      });

      setPeople(response.data);
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };

  // Fetch data when component mounts
  useEffect(() => {
    getUserData();
  }, []);

  return (
    <div>
      {/* Top Navigation */}
      <TopNav setPeople={setPeople} />

      {/* User Count */}
      <InfoSection people={people} />

      {/* User Cards */}
      <div style={{ padding: "30px" }}>
        {people.map((person) => (
          <PersonCard key={person.id} person={person} />
        ))}
      </div>
    </div>
  );
}

export default GithubProject;
