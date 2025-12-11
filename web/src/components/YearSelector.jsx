import { useStatistics } from "../context/StatisticsContext";

function YearSelector({ year, setYear }) {
  const { prev, next } = useStatistics();

  return (
    <div className="flex gap-4 items-center">
      <button disabled={!prev} onClick={() => setYear(year - 1)}>
        ←
      </button>

      <span>{year}</span>

      <button disabled={!next} onClick={() => setYear(year + 1)}>
        →
      </button>
    </div>
  );
}

export default YearSelector;
