import { useEffect, useState } from "react";
import Navbar from "./Navbar";

function Home(){

  const [places,setPlaces] = useState([]);

  useEffect(()=>{

    fetch("https://app-du-lich-2.onrender.com/api/user/auth/places")
      .then(res => res.json())
      .then(data => setPlaces(data))
      .catch(err => console.log(err));

  },[]);

  return(

    <div>

      <Navbar/>

      <div style={styles.container}>

        <h1>Places</h1>

        <div style={styles.grid}>

          {places.map((place)=>(
            
            <div key={place.id} style={styles.card}>

              <img
                src={place.thumbnail}
                alt={place.name}
                style={styles.image}
              />

              <h3>{place.name}</h3>

              <p>{place.city}</p>

              <p>{place.address}</p>

            </div>

          ))}

        </div>

      </div>

    </div>

  )

}

const styles = {

  container:{
    padding:"40px"
  },

  grid:{
    display:"grid",
    gridTemplateColumns:"repeat(3,1fr)",
    gap:"20px",
    marginTop:"20px"
  },

  card:{
    border:"1px solid #ddd",
    borderRadius:"10px",
    padding:"15px",
    textAlign:"center",
    background:"white"
  },

  image:{
    width:"100%",
    height:"180px",
    objectFit:"cover",
    borderRadius:"8px"
  }

};

export default Home;