import * as React from 'react';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';

import axios from 'axios'


const columns = [
  { id: 'name', label: 'Name', minWidth: 170 },
  { id: 'code', label: 'ISO\u00a0Code', minWidth: 100 },
];

function createData(name, code) {
  return { name, code };
}

const rows = [
  createData('India', 1),
  createData('China', 2),
  createData('Italy', 4),
  createData('United States', 5),
  createData('Canada', 8),
  createData('Australia', 'AU'),
  createData('Germany', 'DE'),
  createData('Ireland', 'IE'),
  createData('Mexico', 'MX'),
  createData('Japan', 'JP'),
  createData('France', 'FR'),
  createData('United Kingdom', 'GB'),
  createData('Russia', 'RU'),
  createData('Nigeria', 'NG'),
  createData('Brazil', 'BR'),
];

export default function StickyHeadTable(props) {
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);
  const [rowsData, setRowsData] = React.useState([{name: "Loading"}]);


  React.useEffect(() => {
    const get_freq_data = {
      "start_time": "2011-09-22T14:26:14.000Z",
      "end_time": "2022-10-23T14:26:14.980Z",
      "screen_name": props.search_words,
      "choice": ["word"]
    }
    console.log("FreqTable Trying to connect to API: " + props.search_words)
    axios.post('https://api.theysay.tech/wf',
      get_freq_data)
      .then(res => {
        // console.log(res['data']['data'])
        var w_array_format = []
        let w_array = res.data.data.word;

        for (var i = 0; i < w_array.length; i++)
            {
              w_array_format.push(createData(w_array[i][0], w_array[i][1]))
            }
        setRowsData(w_array_format)
      })
      .catch(err => console.log(err))
  }, [])



  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };

  return (
    <Paper sx={{ width: '100%', overflow: 'hidden' }}>
      <TableContainer sx={{ maxHeight: 440 }}>
        <Table stickyHeader aria-label="sticky table">
          <TableHead>
            <TableRow>
              {columns.map((column) => (
                <TableCell
                  key={column.id}
                  align={column.align}
                  style={{ minWidth: column.minWidth }}
                >
                  {column.label}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {rowsData
              .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
              .map((row) => {
                return (
                  <TableRow hover role="checkbox" tabIndex={-1} key={row.name}>
                    {columns.map((column) => {
                      const value = row[column.id];
                      return (
                        <TableCell key={column.id} align={column.align}>
                          {column.format && typeof value === 'number'
                            ? column.format(value)
                            : value}
                        </TableCell>
                      ); 
                    })}
                  </TableRow>
                );
              })}
          </TableBody>
        </Table>
      </TableContainer>
      <TablePagination
        rowsPerPageOptions={[10, 25, 100]}
        component="div"
        count={rowsData.length}
        rowsPerPage={rowsPerPage}
        page={page}
        onPageChange={handleChangePage}
        onRowsPerPageChange={handleChangeRowsPerPage}
      />
    </Paper>
  );
}
