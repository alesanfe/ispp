import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { TaskPage } from "./pages/TaskPage";
import { TaskFormPage } from "./pages/TaskFormPage";
import CustomDesign from "./components/CustomDesign.jsx";
import { Navigation } from "./components/Navigation";

function App() {
  return (
    <BrowserRouter>
      <Navigation />

      <Routes>
        <Route path="/" element={<Navigate to="/tasks" />} />
        <Route path="/tasks" element={<TaskPage />} />
        <Route path="/tasks-create" element={<TaskFormPage />} />
        <Route path="/designs/my-design" element={<CustomDesign />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
