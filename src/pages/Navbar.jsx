import { Link } from "react-router-dom";

function Navbar(){

  return(

    <div style={styles.navbar}>

      <h2 style={styles.logo}>MyWebsite</h2>

      <div style={styles.links}>

        <Link style={styles.link} to="/">
          Home
        </Link>

        <Link style={styles.link} to="/login">
          Login
        </Link>

        <Link style={styles.link} to="/register">
          Register
        </Link>

      </div>

    </div>

  )

}

const styles = {

  navbar:{
    width:"100%",
    height:"60px",
    display:"flex",
    justifyContent:"space-between",
    alignItems:"center",
    padding:"0 40px",
    background:"#2563eb",
    color:"white",
    boxSizing:"border-box"
  },

  logo:{
    margin:0
  },

  links:{
    display:"flex",
    gap:"20px"
  },

  link:{
    color:"white",
    textDecoration:"none",
    fontWeight:"bold"
  }

};

export default Navbar;