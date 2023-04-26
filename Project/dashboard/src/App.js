import './App.css';
import About from './Views/about';
import Home from './Views/home';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Stats from './Views/statistics';

function App() {
  return (
    // To be removed
    // <div className="App">
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/finder" element={<Stats />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
