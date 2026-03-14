import { useState } from "react";

export default function Register() {

  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: ""
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch("https://app-du-lich-2.onrender.com/api/user/auth/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
      });

      const data = await res.json();

      if (res.ok) {
        setMessage("Register successful");
      } else {
        setMessage(data.detail || "Register failed");
      }

    } catch (error) {
      setMessage("Cannot connect to server");
    }
  };

  return (

    <div className="container d-flex justify-content-center align-items-center vh-100">

      <div className="card shadow p-4" style={{width:"400px"}}>

        <h3 className="text-center mb-4">Create Account</h3>

        <form onSubmit={handleSubmit}>

          <div className="mb-3">
            <label className="form-label">Username</label>
            <input
              name="username"
              className="form-control"
              placeholder="Enter username"
              onChange={handleChange}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Email</label>
            <input
              name="email"
              type="email"
              className="form-control"
              placeholder="Enter email"
              onChange={handleChange}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Password</label>
            <input
              name="password"
              type="password"
              className="form-control"
              placeholder="Enter password"
              onChange={handleChange}
              required
            />
          </div>

          <button className="btn btn-primary w-100">
            Register
          </button>

        </form>

        {message && (
          <div className="alert alert-info mt-3 text-center">
            {message}
          </div>
        )}

      </div>

    </div>
  );
}