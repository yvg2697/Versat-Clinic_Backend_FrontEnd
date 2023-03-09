import React, { useContext } from "react";
import { AuthContext } from "../auth/AuthContext";
import { Navigate } from "react-router-dom";

export const PublicRouter = ({ children }) => {
  const { user } = useContext(AuthContext);

  return user.logged ? <Navigate to="/versat-clinic/dashboard" /> : children;
};
