import Dashboard from "../../components/Dashboard";
import React from "react";
import { Routes, Route, BrowserRouter } from "react-router-dom";
import { Paperbase } from "../dashboard/Dashboard";
export const DashboardRouter = () => {
  return (
    <Routes>
      <Route path="" element={<Dashboard />} />
      {/* <Route path="autenticacion" element={<Paperbase id="aut" />} />
      <Route path="trabajadores" element={<Paperbase id="tr" />} /> */}
    </Routes>
  );
};
