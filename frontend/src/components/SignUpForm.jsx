import React, { useState, useEffect, useContext } from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "./form-control/TextField";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import FormControl from "@mui/material/FormControl";
import Select from "./form-control/Select";
import GeoLocation from "../utilities/GeoNames.jsx";
import Swal from "sweetalert2";
import withReactContent from "sweetalert2-react-content";
import { useForm, FormProvider } from "react-hook-form";
import { types } from "../utilities/types";
import { AuthContext } from "../auth/AuthContext";
import { useNavigate } from "react-router-dom";

export default function SignUpForm() {
  const { dispatch } = useContext(AuthContext);
  const navigate = useNavigate();

  const [country, setCountry] = useState("");
  const [state, setState] = useState("");
  const [city, setCity] = useState("");

  const form = useForm({
    defaultValues: {
      firstName: "",
      lastName: "",
      email: "",
      password: "",
      sex: "",
      skin: "",
      category: "",
      scientific_degree: "",
      country: "",
      state: "",
      city: "",
    },
  });

  const handleLogin = () => {
    const action = {
      type: types.logout,
    };
    dispatch(action);
    navigate("/login", {
      replace: true,
    });
  };

  const onSubmit = (data) => {
    console.log(data);
    data.country = country;
    data.state = state;
    data.city = city;
    const MySwal = withReactContent(Swal);
    MySwal.fire({
      icon: "success",
      title: "Success Sign Up",
      showConfirmButton: true,
      timer: 1500,
    });
    const action = {
      type: types.logout,
    };
    dispatch(action);
    navigate("/login", {
      replace: true,
    });
  };

  const onError = (error) => console.log(error);

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <Box
        sx={{
          marginTop: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign up
        </Typography>

        <FormProvider {...form}>
          <form onSubmit={form.handleSubmit(onSubmit, onError)}>
            <Grid container spacing={3} sx={{ mt: 3 }}>
              <Grid item xs={12} sm={6}>
                <TextField
                  name="firstName"
                  label="First Name"
                  rules={{ required: "First Name Required!" }}
                />
              </Grid>

              <Grid item xs={12} sm={6}>
                <TextField
                  name="lastName"
                  label="Last Name"
                  rules={{ required: "Last Name Required!" }}
                />
              </Grid>

              <Grid item xs={12}>
                <TextField
                  fullWidth
                  name="email"
                  label="Email"
                  rules={{
                    required: "Last Name Required!",
                    pattern: {
                      value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
                      message: "Invalid email address",
                    },
                  }}
                />
              </Grid>

              <Grid item xs={12}>
                <TextField
                  fullWidth
                  name="password"
                  label="Password"
                  type="password"
                  rules={{
                    required: "Password Required!",
                    pattern: {
                      value:
                        /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s)(?=.*[!@#$*])/,
                      message:
                        "Password should contain at least one uppercase letter, lowercase letter, digit, and special symbol.",
                    },
                  }}
                />
              </Grid>

              <Grid item xs={12}>
                <FormControl fullWidth>
                  <Select
                    name="sex"
                    label="Sex"
                    rules={{ required: "Sex is Required!" }}
                    items={[
                      { name: "Male", value: 1 },
                      { name: "Female", value: 2 },
                      { name: "Not Binary", value: 3 },
                    ]}
                  />
                </FormControl>
              </Grid>

              <Grid item xs={12}>
                <FormControl fullWidth>
                  <Select
                    name="skin"
                    label="Skin Color"
                    rules={{ required: "Skin Color is Required!" }}
                    items={[
                      { name: "Caucasico", value: 1 },
                      { name: "Moreno", value: 2 },
                      { name: "Otro", value: 3 },
                    ]}
                  />
                </FormControl>
              </Grid>

              <Grid item xs={12}>
                <FormControl fullWidth>
                  <Select
                    name="category"
                    label="Category"
                    rules={{ required: "Category is Required!" }}
                    items={[
                      { name: "Category 1", value: 1 },
                      { name: "Category 2", value: 2 },
                      { name: "Category 3", value: 3 },
                    ]}
                  />
                </FormControl>
              </Grid>

              <Grid item xs={12}>
                <FormControl fullWidth>
                  <Select
                    name="scientific_degree"
                    label="Scientific Degree"
                    rules={{ required: "Scientific Degree is Required!" }}
                    items={[
                      { name: "Scientific Degree 1", value: 1 },
                      { name: "Scientific Degree 2", value: 2 },
                      { name: "Scientific Degree 3", value: 3 },
                    ]}
                  />
                </FormControl>
              </Grid>

              <Grid item xs={12}>
                <FormControl fullWidth sx={{ mb: 3 }}>
                  <GeoLocation
                    name="country"
                    locationTitle="Country"
                    isCountry
                    onChange={setCountry}
                  />
                </FormControl>
                <FormControl fullWidth sx={{ mb: 3 }}>
                  <GeoLocation
                    locationTitle="State"
                    onChange={setState}
                    geoId={country}
                  />
                </FormControl>
                <FormControl fullWidth sx={{ mb: 3 }}>
                  <GeoLocation
                    locationTitle="City"
                    onChange={setCity}
                    geoId={state}
                  />
                </FormControl>
              </Grid>

              <Grid container justifyContent="flex-end">
                <Grid item>
                  <Link href="#" variant="body2" onClick={handleLogin}>
                    Already have an account? Sign in
                  </Link>
                </Grid>
              </Grid>
            </Grid>

            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 2, mb: 2 }}
            >
              Sign Up
            </Button>
          </form>
        </FormProvider>
      </Box>
    </Container>
  );
}
