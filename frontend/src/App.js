import React, {useEffect, useState} from "react";
import PostCard from "./components/PostCard";

function App(){
  const [posts, setPosts] = useState([]);
  const [q, setQ] = useState("");
  const [loading, setLoading] = useState(false);
  const [sort, setSort] = useState("new");

  useEffect(()=>{
    fetchPosts();
  }, [sort]);

  async function fetchPosts(){
    setLoading(true);
    try {
      const res = await fetch(`/api/posts?sort=${sort}`);
      const json = await res.json();
      if(json.status === "ok"){
        setPosts(json.posts);
      } else {
        console.error(json.message);
      }
    } catch(err){
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  const filtered = posts.filter(p =>
    p.title.toLowerCase().includes(q.toLowerCase()) || (p.selftext || "").toLowerCase().includes(q.toLowerCase())
  );

  return (
    <div style={{maxWidth:900, margin:"20px auto", fontFamily:"Arial, sans-serif"}}>
      <h1>r/SideProject Feed</h1>

      <div style={{display:"flex", gap:8, marginBottom:12}}>
        <input placeholder="Search titles..." value={q} onChange={e=>setQ(e.target.value)} style={{flex:1, padding:8}} />
        <select value={sort} onChange={e=>setSort(e.target.value)} style={{padding:8}}>
          <option value="new">Newest</option>
          <option value="ups">Top (ups)</option>
          <option value="comments">Top (comments)</option>
        </select>
        <button onClick={fetchPosts} style={{padding:"8px 12px"}}>Refresh</button>
      </div>

      {loading ? <p>Loading...</p> : filtered.length === 0 ? <p>No posts</p> :
        filtered.map(p => <PostCard key={p.id} post={p} />)
      }
    </div>
  );
}

export default App;
