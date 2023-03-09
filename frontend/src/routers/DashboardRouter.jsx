import React from 'react'
import {Routes,Route, BrowserRouter} from "react-router-dom"
import Dashboard from "../components/Dashboard"
export const DashboardRouter = () => {
  return (
    
      <Routes>
      
        <Route path='' element={<Dashboard />}/>
       

      </Routes>

  )
}
