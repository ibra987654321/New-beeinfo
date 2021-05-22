let input = document.getElementById('login__input');
let pass = document.getElementById('login__input_pass');
let span = document.getElementById('login__span')
let span_pass = document.getElementById('login__span_pass')
let btn = document.getElementById('login__btn')
let data = document.querySelectorAll('span[data-placeholder]')

input.addEventListener("blur", () => {
    if(input.value != "") {
        input.classList.add('has-val');
        btn.classList.add('login__btn_active')
        }
    else {
        input.classList.remove('has-val');
        btn.classList.remove('login__btn_active')
        }
       
}, true)

pass.addEventListener("blur", () => {
    if(pass.value != "") {
        pass.classList.add('has-val');
       
        }
    else {
        pass.classList.remove('has-val');
        }
       
}, true)

// обработка ошибок формы
let form = document.getElementById('login__form')
let fields = document.getElementsByClassName('login__input')

//   Чистка классов
const removeValidation = function () {
    let errors = form.querySelectorAll('.login-error')
  
    for (let i = 0; i < errors.length; i++) {
      errors[i].remove()
    }
  }
// Проверка полей
const checkFieldsPresence = function(){
    for (let i = 0; i < fields.length; i++) {
        if(!fields[i].value){
            let error = document.createElement('div')
            error.className = 'login-error'
            error.style.color = 'red'
            error.style.textAlign = 'right'
            error.innerHTML = 'Поле не может быть пустым'
            form[i].parentElement.insertBefore(error, fields[i])
        }
        
    }
}

// Валидация  пароля
const checkPasswordMatch = function() {
    if (pass.value !== passwordInDataBase && pass.value != "" ) {
        console.log('not equals')
        let error = document.createElement('div')
        error.className = 'login-error'
        error.style.color = 'red'
        error.innerHTML = 'Пароль не верный'
        pass.parentElement.insertBefore(error, pass)
      }
}

// Валидация  логина
const checkLogin = function() {
    if (input.value !== loginInDataBase && input.value != "") {
        console.log('not equals')
        let error = document.createElement('div')
        error.className = 'login-error'
        error.style.color = 'red'
        error.innerHTML = 'Корпоративная почта не в базе'
        input.parentElement.insertBefore(error, input)
      }
}

form.addEventListener('submit', function (event) {
    event.preventDefault()

    removeValidation()

    checkFieldsPresence()

    checkPasswordMatch()
    
    checkLogin()
  })

//   Пример для проверки
  const passwordInDataBase = '12345';
  const loginInDataBase = 'Admin';