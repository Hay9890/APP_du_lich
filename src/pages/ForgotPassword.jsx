import { useState } from "react";

function ForgotPassword(){

  const [email,setEmail] = useState("");
  const [otp,setOtp] = useState("");
  const [newPassword,setNewPassword] = useState("");
  const [message,setMessage] = useState("");

  const sendOtp = async ()=>{

    const res = await fetch(
      "https://app-du-lich-2.onrender.com/api/user/auth/forgot",
      {
        method:"POST",
        headers:{
          "Content-Type":"application/json"
        },
        body:JSON.stringify({email})
      }
    );

    const data = await res.json();

    if(res.ok){
      setMessage("OTP sent to email 📧");
    }else{
      setMessage(data.detail);
    }

  };

  const resetPassword = async (e)=>{

    e.preventDefault();

    const res = await fetch(
      "https://app-du-lich-2.onrender.com/api/user/auth/reset",
      {
        method:"POST",
        headers:{
          "Content-Type":"application/json"
        },
        body:JSON.stringify({
          email,
          otp,
          new_password:newPassword
        })
      }
    );

    const data = await res.json();

    if(res.ok){
      setMessage("Password reset success 🎉");
    }else{
      setMessage(data.detail);
    }

  };

  return(

    <div style={styles.container}>

      <form style={styles.card} onSubmit={resetPassword}>

        <h2>Reset Password</h2>

        <label>Email</label>

        <input
          style={styles.input}
          value={email}
          onChange={(e)=>setEmail(e.target.value)}
        />

        <button
          type="button"
          style={styles.button}
          onClick={sendOtp}
        >
          Send OTP
        </button>

        <label>OTP</label>

        <input
          style={styles.input}
          value={otp}
          onChange={(e)=>setOtp(e.target.value)}
        />

        <label>New Password</label>

        <input
          style={styles.input}
          type="password"
          value={newPassword}
          onChange={(e)=>setNewPassword(e.target.value)}
        />

        <button style={styles.button}>
          Reset Password
        </button>

        {message && <p>{message}</p>}

      </form>

    </div>

  )

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
  }

};

export default ForgotPassword;