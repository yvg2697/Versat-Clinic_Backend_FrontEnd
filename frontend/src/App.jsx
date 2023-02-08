import React, { useEffect, useReducer } from "react";
// import SignIn from "./components/SignIn";
// import SignUpForm from "./components/SignUpForm";
// import Dashboard from "./components/Dashboard";

// export function App() {
//   return (
//     <>
//       {/* <Dashboard/> */}
//       <SignIn/>
//       {/* <SignUpForm /> */}
//     </>
//   );
// }

import { AppRouter } from "./routers/AppRouter";
import { AuthContext } from "./auth/AuthContext";
import { authReducer } from "./auth/authReducer";

const init = () => {
  return JSON.parse(localStorage.getItem("user")) || { logged: false };
};

export const App = () => {
  const [user, dispatch] = useReducer(authReducer, {}, init);
  useEffect(() => {
    if (!user) return;

    localStorage.setItem("user", JSON.stringify(user));
  }, [user]);
  return (
    <AuthContext.Provider
      value={{
        user,
        dispatch,
      }}
    >
      <AppRouter />
    </AuthContext.Provider>
  );
};
