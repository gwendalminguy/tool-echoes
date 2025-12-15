import { useState, useEffect } from "react";

function TopCard({ cardClass, name, data }) {
  const [page, setPage] = useState(0);
  const pageSize = 5;

  if (!data) return <div className={cardClass}>No Data</div>;

  const pageCount = Math.ceil(data.length / pageSize);

  const startIndex = page * pageSize + 1;

  const pageData = data.slice(
    page * pageSize,
    page * pageSize + pageSize
  );

  useEffect(() => {
    setPage(0);
  }, [data]);

  return (
    <div className={`${cardClass} flex flex-col justify-between`}>
      <div className="">
        <h2 className="text-lg font-semibold mb-4">{name}</h2>

        {/* Data */}
        <ul className="list space-y-2">
          {pageData.map((item, index) => (
            <li key={page * pageSize + index} className="list-row pt-1 pb-3">
              <div className="text-3xl font-thin opacity-50 tabular-nums">
                {String(page * pageSize + index + 1).padStart(2, "0")}
              </div>
              <div className="list-col-grow">
                <div className="text-sm font-medium">{item.primary}</div>
                <div className="text-xs uppercase font-semibold opacity-50">{item.secondary}</div>
              </div>
            </li>
          ))}
        </ul>
      </div>

      {/* Pagination */}
      <div className="flex justify-evenly items-center mt-4 text-sm">
        <button disabled={page === 0} onClick={() => setPage((p) => p - 1)} className={`px-2 cursor-pointer ${page === 0 && "text-gray-400"}`}>
          ←
        </button>

        <div className="flex flex-row gap-5">
        {[...Array(pageCount)].map((_, index) => (
          <button key={index} onClick={() => setPage(index)} className={`w-3 h-3 rounded-full transition-all duration-300 cursor-pointer ${index === page ? "bg-primary" : "bg-primary/20"}`} />
        ))}
        </div>

        <button disabled={page === pageCount - 1} onClick={() => setPage((p) => p + 1)} className={`px-2 cursor-pointer ${page === pageCount - 1 && "text-gray-400"}`}>
          →
        </button>
      </div>
    </div>
  );
}

export default TopCard;
