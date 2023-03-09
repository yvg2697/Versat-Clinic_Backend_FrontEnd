import React from "react";
import { Routes, Route, BrowserRouter } from "react-router-dom";
import { DashboardRouter } from "./DashboardRouter";
import SignIn from "../components/SignIn";
import SignUpForm from "../components/SignUpForm";
import { PrivateRouter } from "./PrivateRouter";
import { PublicRouter } from "./PublicRouter";

export const AppRouter = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="versat-clinic/login"
          element={
            <PublicRouter>
              <SignIn />
            </PublicRouter>
          }
        />
        <Route
          path="versat-clinic/"
          element={
            <PublicRouter>
              <SignIn />
            </PublicRouter>
          }
        />

        <Route
          path="versat-clinic/sign_up"
          element={
            <PublicRouter>
              <SignUpForm />
            </PublicRouter>
          }
        />

        <Route
          path="versat-clinic/dashboard/*"
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
