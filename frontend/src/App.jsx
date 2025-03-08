import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import AIProjects from "./pages/AIProjects";
import SoftwareTools from "./pages/SoftwareTools";
import PhysicalProjects from "./pages/PhysicalProjects";
import Navbar from "./components/Navbar";
import "./App.css";

function App() {
    return (
        <>
            <Navbar />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/ai-projects" element={<AIProjects />} />
                <Route path="/software-tools" element={<SoftwareTools />} />
                <Route path="/physical-projects" element={<PhysicalProjects />} />
            </Routes>
        </>
    );
}

export default App;