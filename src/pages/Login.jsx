import { useState } from "react";
import { Link } from "react-router-dom";

function Login() {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e) => {

    e.preventDefault();

    setLoading(true);
    setMessage("");

    try {

      const res = await fetch(
        "https://app-du-lich-2.onrender.com/api/user/auth/login",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            email,
            password
          })
        }
      );

      const data = await res.json();

      if (res.ok) {

        localStorage.setItem("token", data.access_token);

        setMessage("Login success 🎉");

      } else {

        setMessage(data.detail || "Login failed");

      }

    } catch {

      setMessage("Server error ❌");

    }

    setLoading(false);

  };

  return (

    <div style={styles.container}>

      <form style={styles.card} onSubmit={handleLogin}>

        <h2 style={styles.title}>Login</h2>

        <label>Email</label>
        <input
          style={styles.input}
          type="email"
          value={email}
          onChange={(e)=>setEmail(e.target.value)}
          required
        />

        <label>Password</label>
        <input
          style={styles.input}
          type="password"
          value={password}
          onChange={(e)=>setPassword(e.target.value)}
          required
        />

        <button style={styles.button} disabled={loading}>
          {loading ? "Logging in..." : "Login"}
        </button>

        {message && <p>{message}</p>}

        <div style={styles.links}>

          <Link to="/forgot">
            Forgot password?
          </Link>

        </div>

      </form>

    </div>

  );

}

const styles = {

  container:{
    height:"100vh",
    display:"flex",
    justifyContent:"center",
    alignItems:"center",
    background:"#f4f6f8"
  },

  card:{
    width:"320px",
    padding:"30px",
    background:"white",
    borderRadius:"10px",
    display:"flex",
    flexDirection:"column",
    gap:"10px"
  },

  input:{
    padding:"10px",
    border:"1px solid #ccc"
  },

  button:{
    padding:"10px",
    background:"#2563eb",
    color:"white",
    border:"none"
  },

  links:{
    marginTop:"10px"
  }

};

export default Login;