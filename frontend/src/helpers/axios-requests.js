import axios from 'axios';

export const getUsers=(setWorkers)=>{
    axios.get('http://localhost:8000/versat-clinic/api/trabajador/', {
    responseType: 'json'
  })
    .then(function(res) {
      if(res.status==200) {
        console.log(res.data);
        setWorkers(res.data);
        
      }
      console.log(res);
    })
    .catch(function(err) {
      console.log(err);
    })
    .then(function() {
      ;
    });
}