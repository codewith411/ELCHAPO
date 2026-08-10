import { useState } from "react";
import axios from "axios";

function TopNav({ setPeople }) {
  const [search, setSearch] = useState("");

  const onSearch = async () => {
    try {
      const trimmedString = search.trim();

      if (trimmedString === "" || trimmedString.length < 3) {
        return;
      }

      const response = await axios({
        method: "GET",
        url: "https://api.github.com/search/users",
        headers: {
          Authorization: `Bearer ${import.meta.env.VITE_GITHUB_TOKEN}`,
          Accept: "application/vnd.github+json",
        },
        params: {
          q: trimmedString,
        },
      });

      setPeople(response.data.items);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        padding: "20px",
      }}
    >
      <img
        src="https://toppng.com/uploads/preview/github-logo-png-photo-11659780047rlwsegmg72.png"
        alt="GitHub"
        style={{ width: "40px" }}
      />

      <input
        type="text"
        placeholder="Search GitHub..."
        style={{
          width: "50vw",
          marginLeft: "1rem",
        }}
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <button onClick={onSearch}>Search</button>
    </div>
  );
}

export default TopNav;
