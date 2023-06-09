const form = document.getElementById('myForm');
const comision = document.getElementById('comision');
const swap = document.getElementById('swap');
let timeoutId;

const enviarFormulario = () => {
  form.submit();
};

comision.addEventListener('blur', enviarFormulario);
swap.addEventListener('blur', enviarFormulario);


  const comisionInput = document.getElementById('comision');
  comisionInput.addEventListener('input', () => {
    let value = comisionInput.value.trim();
  
    // Verificamos si el primer carácter es un número
    if (/^\d/.test(value)) {
      // Añadimos el signo menos al principio del valor
      value = '-' + value;
    }    
  
    comisionInput.value = value;
  });


  const swapInput = document.getElementById('swap');
  swapInput.addEventListener('input', () => {
    let value = swapInput.value.trim();
  
    // Verificamos si el primer carácter es un número
    if (/^\d/.test(value)) {
      // Añadimos el signo menos al principio del valor
      value = '-' + value;
    }
  
    swapInput.value = value;
  });
  
 