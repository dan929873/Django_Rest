import React from 'react'

const TODOItem = ({todo}) => {
    return(
    <tr>
        <td>{todo.project}</td>
        <td>{todo.note_text}</td>
        <td>{todo.data_create}</td>
        <td>{todo.data_cheng}</td>
        <td>{todo.user_created}</td>
        <td>{todo.activ}</td>
    </tr>
    )
}


const TODOList = ({todos}) => {
    return(
        <table>
        <th>
            project
        </th>
        <th>
            note_text
        </th>
        <th>
            data_create
        </th>
        <th>
            data_cheng
        </th>
        <th>
            user_created
        </th>
        <th>
            activ
        </th>
        {todos.map((todo) => <TODOItem todo={todo} />)}
        </table>
    )
}

export default TODOList