import * as React from 'react';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';




const theme = createTheme();

export default function Album() {
    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <main>
                {/* Hero unit */}
                <Box
                    sx={{
                        bgcolor: 'background.paper',
                        pt: 4,
                        pb: 6,
                    }}
                >
                    <Container maxWidth="sm">
         
                        <Typography
                            component="h1"
                            variant="h5"
                            align="center"
                            color="text.secondary"
                            gutterBottom
                            sx={{ pb: "10%" }}
                        >
                            [No worries this is TheySay's undefined-logo]
                        </Typography>

                        {/* change the img here to define logo */}
                        {/* <Typography
                            component="h1"
                            variant="h5"
                            align="center"
                            color="text.secondary"
                            gutterBottom
                            sx={{ pb: "10%" }}
        
                        >
                            <img src="/logo512.png" style={{width:"15%"}}/>
                        </Typography> */}




                        <Typography variant="h2" align="center" color="" display="inline" sx={{ fontWeight: 400 }}>
                            Get&nbsp;
                        </Typography>
                        <Typography variant="h2" align="center" color="SlateBlue" display="inline" sx={{ fontWeight: 900 }}>
                            Insights
                        </Typography>


                        <Typography variant="h2" align="center" color="" sx={{ fontWeight: 400 }}>
                            from social media.
                        </Typography>

                    </Container>
                </Box>

            </main>
            {/* End footer */}
        </ThemeProvider>
    );

}