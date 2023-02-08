import React from "react";
import { Routes, Route, BrowserRouter } from "react-router-dom";
import { DashboardRouter } from "../config/routers/DashboardRouter";
import SignIn from "../components/SignIn";
import SignUpForm from "../components/SignUpForm";
import { PrivateRouter } from "./PrivateRouter";
import { PublicRouter } from "./PublicRouter";

export const AppRouter = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/login"
          element={
            <PublicRouter>
              <SignIn />
            </PublicRouter>
          }
        />
        <Route
          path="/"
          element={
            <PublicRouter>
              <SignIn />
            </PublicRouter>
          }
        />

        <Route
          path="/sign_up"
          element={
            <PublicRouter>
              <SignUpForm />
            </PublicRouter>
          }
        />

        <Route
          path="/dashboard/*"
          element={
            <PrivateRouter>
              <DashboardRouter />
            </PrivateRouter>
          }
        />
      </Routes>
    </BrowserRouter>
  );
};
