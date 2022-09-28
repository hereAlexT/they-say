
import AppBar from '@mui/material/AppBar';
import Typography from '@mui/material/Typography';
import Toolbar from '@mui/material/Toolbar';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';


export default function Nav() {
    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar position="static">
                <Toolbar>

                    <Typography variant="h6" component="div" sx={{ mr: 2 }}>
                        TheySay
                    </Typography>


                    <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                    </Typography>


                    <Button color="inherit" href="https://github.com/AlexTengT/they-say" target="_blank">Github</Button>
                </Toolbar>
            </AppBar>
        </Box>
    );

}