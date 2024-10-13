import React from "react";
import { useAuth0 } from "@auth0/auth0-react";
import './Profile.css';

const Profile = () => {
  const { user, isAuthenticated, isLoading } = useAuth0();

  if (isLoading) {
    return <div className="profile-loading"><div className="loading-spinner"></div></div>;
  }

  return (
    isAuthenticated && (
      <div className="profile-dropdown">
        <img src={user.picture} alt={user.name} className="profile-picture" />
        <h3 className="profile-name">{user.name}</h3>
        <p className="profile-email">{user.email}</p>
        <p className="profile-id">User ID: {user.sub}</p>
      </div>
    )
  );
};

export default Profile;
