import YearSelector from "./YearSelector";
import ThemeSwitch from "./ThemeSwitch";

function Navbar({ year, setYear }) {
  return (
    <nav className="navbar fixed top-0 left-0 w-full backdrop-blur-md bg-base-100/70 border-b border-base-300/70 shadow-sm z-100 h-20 transition-all duration-300">
      <div className="max-w-screen-7xl mx-auto px-4 h-full flex justify-between items-center w-full">
        {/* Title */}
        <h1 className="text-2xl text-primary font-bold hover:text-primary/90">
          Echoes
        </h1>

        {/* Year Selector */}
        <YearSelector year={year} setYear={setYear} />

        {/* Theme Switch */}
        <ThemeSwitch />
      </div>
    </nav>
  );
}

export default Navbar;
