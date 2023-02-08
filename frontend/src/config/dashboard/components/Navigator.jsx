import * as React from "react";
import Divider from "@mui/material/Divider";
import Drawer from "@mui/material/Drawer";
import List from "@mui/material/List";
import Box from "@mui/material/Box";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import HomeIcon from "@mui/icons-material/Home";
import PeopleIcon from "@mui/icons-material/People";
import Diversity3Rounded from "@mui/icons-material/Diversity3Rounded";
import MedicalServicesRounded from "@mui/icons-material/MedicalServicesRounded";
import LocalHotelRounded from "@mui/icons-material/LocalHotelRounded";
import SchoolRounded from "@mui/icons-material/SchoolRounded";
import AssistWalker from "@mui/icons-material/AssistWalker";
import TimerIcon from "@mui/icons-material/Timer";
import MonitorHeartRounded from "@mui/icons-material/MonitorHeartRounded";
import AirlineSeatFlat from "@mui/icons-material/AirlineSeatFlat";
import { NavLink } from "react-router-dom";

const categories = [
  {
    id: "Admin",
    children: [
      {
        id: "Autenticación",
        path: "autenticacion",
        icon: <PeopleIcon />,
        active: true,
      },
      { id: "Trabajadores", icon: <Diversity3Rounded />, path: "trabajadores" },
      { id: "Especialidades", icon: <SchoolRounded /> },
      { id: "Salas", icon: <LocalHotelRounded /> },
      { id: "Servicios", icon: <MedicalServicesRounded /> },
    ],
  },
  {
    id: "Estadísticas",
    children: [
      { id: "Consultas externas", icon: <AssistWalker /> },
      { id: "Procedimientos quirúrgicos", icon: <MonitorHeartRounded /> },
      { id: "Control de ingresos", icon: <AirlineSeatFlat /> },
    ],
  },
];

const item = {
  py: "2px",
  px: 3,
  color: "rgba(255, 255, 255, 0.7)",
  "&:hover, &:focus": {
    bgcolor: "rgba(255, 255, 255, 0.08)",
  },
};

const itemCategory = {
  boxShadow: "0 -1px 0 rgb(255,255,255,0.1) inset",
  py: 1.5,
  px: 3,
};

export default function Navigator(props) {
  const { ...other } = props;

  return (
    <Drawer variant="permanent" {...other}>
      <List disablePadding>
        <ListItem
          sx={{ ...item, ...itemCategory, fontSize: 22, color: "#fff" }}
        >
          Versat Clinica
        </ListItem>
        <ListItem sx={{ ...item, ...itemCategory }}>
          <ListItemIcon>
            <HomeIcon />
          </ListItemIcon>
          <ListItemText>Descripción general</ListItemText>
        </ListItem>
        {categories.map(({ id, children }) => (
          <Box key={id} sx={{ bgcolor: "#101F33" }}>
            <ListItem sx={{ py: 2, px: 3 }}>
              <ListItemText sx={{ color: "#fff" }}>{id}</ListItemText>
            </ListItem>
            {children.map(({ id: childId, icon, active, path }) => (
              <NavLink
                activeClassName="active"
                to={"/dashboard/" + path}
                className="nav-item nav-link"
              >
                <ListItem disablePadding key={childId}>
                  <ListItemButton sx={item}>
                    <ListItemIcon>{icon}</ListItemIcon>

                    <ListItemText>{childId}</ListItemText>
                  </ListItemButton>
                </ListItem>
              </NavLink>
            ))}

            <Divider sx={{ mt: 2 }} />
          </Box>
        ))}
      </List>
    </Drawer>
  );
}
