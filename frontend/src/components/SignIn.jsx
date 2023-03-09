import React, { useContext } from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "./form-control/TextField";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import Swal from "sweetalert2";
import withReactContent from "sweetalert2-react-content";
import { useForm, FormProvider } from "react-hook-form";
import { Link } from "@mui/material";
import { types } from "../utilities/types";
import { AuthContext } from "../auth/AuthContext";
import { useNavigate } from "react-router-dom";

export default function SignIn() {
  const { dispatch } = useContext(AuthContext);
  const navigate = useNavigate();

  const form = useForm({
    defaultValues: {
      email: "",
      password: "",
    },
  });

  const handleSignUp = () => {
    const action = {
      type: types.sign_up,
    };
    dispatch(action);
    navigate("/versat-clinic/sign_up", {
      replace: true,
    });
  };

  const onSubmit = (data) => {
    console.log(data);
    const MySwal = withReactContent(Swal);
    MySwal.fire({
      icon: "success",
      title: "Success Sign In",
      showConfirmButton: false,
      timer: 1000,
    });

    const action = {
      type: types.login,
      payload: { name: data.email },
    };

    dispatch(action);
    navigate("/versat-clinic/dashboard", {
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
          Sign In
        </Typography>

        <FormProvider {...form}>
          <form onSubmit={form.handleSubmit(onSubmit, onError)}>
            <Grid container spacing={3} sx={{ mt: 3 }}>
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
            </Grid>

            <Grid container justifyContent="flex-end">
              <Grid item sx={{ mt: 2 }}>
                <Link href="#" variant="body2" onClick={handleSignUp}>
                  Dont have an account? Sign Up
                </Link>
              </Grid>
            </Grid>

            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 2, mb: 2 }}
            >
              Sign In
            </Button>
          </form>
        </FormProvider>
      </Box>
    </Container>
  );
}
