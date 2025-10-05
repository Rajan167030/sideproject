import React from "react";

export default function PostCard({post}) {
  return (
    <div style={{border:"1px solid #ddd", padding:12, borderRadius:8, marginBottom:10}}>
      <a href={post.permalink} target="_blank" rel="noreferrer">
        <h3 style={{margin:0}}>{post.title}</h3>
      </a>
      <p style={{margin:"6px 0"}}>by <strong>{post.author}</strong> • {post.ups} ups • {post.num_comments} comments</p>
      {post.thumbnail && <img src={post.thumbnail} alt="" style={{maxWidth:120}} />}
      {post.selftext && <p style={{marginTop:8}}>{post.selftext.slice(0,200)}{post.selftext.length>200?"...":""}</p>}
    </div>
  );
}
