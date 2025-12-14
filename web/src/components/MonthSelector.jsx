function MonthSelector({ allMonths, selectedMonth, setSelectedMonth }) {
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
      <button disabled={!hasPrev} onClick={() => update(-1)} className={`hover:cursor-pointer ${!hasPrev && "text-gray-400"}`}>
        ←
      </button>

      <span className="bg-base-200 px-3 py-1 rounded-full w-30 text-center">{monthName}</span>

      <button disabled={!hasNext} onClick={() => update(1)} className={`hover:cursor-pointer ${!hasNext && "text-gray-400"}`}>
        →
      </button>
    </div>
  );
}

export default MonthSelector;
