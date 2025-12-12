import { useStatistics } from "../context/StatisticsContext";

function YearSelector({ year, setYear }) {
  const { prev, next } = useStatistics();

  return (
    <div className="flex gap-4 items-center">
      <button disabled={!prev} onClick={() => setYear(year - 1)} className={`hover:cursor-pointer ${!prev && "text-gray-400"}`}>
        ←
      </button>

      <span className="bg-base-200 px-3 py-1 rounded-full">{year}</span>

      <button disabled={!next} onClick={() => setYear(year + 1)} className={`hover:cursor-pointer ${!next && "text-gray-400"}`}>
        →
      </button>
    </div>
  );
}

export default YearSelector;
