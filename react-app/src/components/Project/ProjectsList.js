import { useSelector } from "react-redux";
import { NavLink } from "react-router-dom";

export default function ProjectsList() {
    const projects = useSelector(state => Object.values(state.projects));

    const projectComponents = projects?.map(project => {
        return (
            <li key={project?.id}>
                <NavLink to={`/projects/${project?.id}`}>{project?.name} - {project?.key}</NavLink>
            </li>
        );
    });

    return (
        <>
            <h1>Project List:</h1>
            <ul>{projectComponents}</ul>
        </>
    )
}