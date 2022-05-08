import {useParams} from 'react-router-dom'
import React from 'react'

const ProjectItem = ({project}) => {
    return(
    <tr>
        <td>{project.name}</td>
        <td>{project.link}</td>
        <td>{project.users}</td>
    </tr>
    )
}


const ProjectList = ({projects}) => {

    return(
        <table>
        <th>
            name
        </th>
        <th>
            link
        </th>
        <th>
            users
        </th>
        {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList