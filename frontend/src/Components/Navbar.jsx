import { Link } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
    return (
        <nav>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/ai-projects">AI Projects</Link></li>
                <li><Link to="/software-tools">Software Tools</Link></li>
                <li><Link to="/physical-projects">Physical Projects</Link></li>
            </ul>
        </nav>
    );
}

export default Navbar;