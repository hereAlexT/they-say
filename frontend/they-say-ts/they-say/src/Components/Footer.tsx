import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Link from '@mui/material/Link';
import { createTheme, ThemeProvider } from '@mui/material/styles';

function Copyright() {
    return (
        <Typography variant="body2" color="text.secondary" align="center">
            {'Copyright © '}
            <Link color="inherit" href="https://theysay.tech/">
                TheySay.tech
            </Link>{' '}
            {new Date().getFullYear()}
            {'.'}
        </Typography>
    );
}


export default function Footer() {
    return (
        <Box sx={{ bgcolor: 'background.paper', p: 6 }} component="footer">
            {/* <Typography variant="h6" align="center" gutterBottom>
                TheySay.Tech
            </Typography> */}
            <Typography
                variant="subtitle1"
                align="center"
                color="text.secondary"
                component="p"
            >
                TheySay.Tech
            </Typography>
            <Copyright />
        </Box>
    )
}