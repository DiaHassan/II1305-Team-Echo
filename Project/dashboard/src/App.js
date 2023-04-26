import './App.css';
import About from './Views/about';
import Home from './Views/home';
import Statistics from './Views/statistics';
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    // To be removed
    // <div className="App">
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          {/* <Route path="/finder" element={<AboutView />} /> */}
          <Route path="/about" element={<About />} />
          <Route path="/statistics" element={<Statistics/>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
