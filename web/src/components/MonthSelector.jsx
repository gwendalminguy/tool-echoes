function MonthSelector({ allMonths, view, selectedMonth, setSelectedMonth }) {
  const monthNumber = Number(selectedMonth);
  const monthName = allMonths.find(m => m.number === selectedMonth)?.name;

  const hasPrev = monthNumber > 1;
  const hasNext = monthNumber < 12;

  const update = (delta) => {
    const nextMonth = monthNumber + delta;
    const padded = String(nextMonth).padStart(2, "0");
    setSelectedMonth(padded);
  };

  return (
    <div className="flex gap-4 items-center justify-center">
      <button
        onClick={() => update(-1)}
        disabled={!hasPrev || view === "months"}
        className={`hover:cursor-pointer ${(!hasPrev || view === "months") && "text-gray-400"}`}
      >
        ←
      </button>

      <span className={`bg-base-200 px-3 py-1 rounded-full w-30 text-center ${view === "months" && "text-gray-400"}`}>
        {monthName}
      </span>

      <button
        onClick={() => update(1)}
        disabled={!hasNext || view === "months"}
        className={`hover:cursor-pointer ${(!hasNext || view === "months") && "text-gray-400"}`}
      >
        →
      </button>
    </div>
  );
}

export default MonthSelector;
