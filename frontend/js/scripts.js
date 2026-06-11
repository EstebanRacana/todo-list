const API_URL="http://127.0.0.1:8000/todos"
const todoInput=document.getElementById("todo-input")
const createBtn=document.getElementById("create-btn")
const todoList=document.getElementById("todo-list")

async function getTodos(){
    console.log("getTodos ejecutado")
    const response=await fetch(API_URL)
    const data=await response.json()
    console.log(data)
    todoList.innerHTML=""
    data.forEach(element => {
        const li=document.createElement("li")
        li.textContent=element.title
      
        
        const deleteBtn=document.createElement("button")
        deleteBtn.textContent="Eliminate"
    

       

        const updateBtn=document.createElement("button")
        updateBtn.textContent="Update"
        



        li.appendChild(deleteBtn)
        li.appendChild(updateBtn)
        todoList.appendChild(li)
       
     deleteBtn.addEventListener("click", () =>{
        deleteTodo(element.id)
        })
        
    updateBtn.addEventListener("click", ()=>{
        const newTask=prompt("New task")
        if(newTask){
            updateTodo(element.id, newTask)
        }
    })
   

    });
}
getTodos()

async function createTodo(){
    const title = todoInput.value
    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ title: title })
    })
    todoInput.value = ""
    getTodos()
}
createBtn.addEventListener("click", createTodo)

async function deleteTodo(id){
    await fetch(`${API_URL}/${id}`, {
        method: "DELETE"
    })
    console.log("deleteTodo ejecutado, llamando getTodos")
    getTodos()
}

async function updateTodo(id, newTask){
    await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ title: newTask })
    })
    getTodos()
}